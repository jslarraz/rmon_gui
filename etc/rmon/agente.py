# -*- coding: utf-8 -*-
# Importamos todo lo necesario
from pysnmp.carrier.asynsock.dispatch import AsynsockDispatcher
from pysnmp.carrier.asynsock.dgram import udp
from pyasn1.codec.ber import encoder, decoder
from pysnmp.proto import api
import MySQLdb
import tools
import mib
import signal


class agente:

    # Funcion de inicializacion
    def __init__(self): 
	global value
	value = 0
     
        # Decimos agente ON
        print "SNMP Service ON"

        # Leemos las opciones del fichero de configuracion
        fd = open("/etc/rmon/rmon.conf")
        line = fd.readline()
        while line:
            if '=' in line:
                substr = line.split('=')
                substr[1] = substr[1].split('\n')
                substr[1] = substr[1][0]

                if substr[0] == "IP_ADDR":
                    self.IP_ADDR = substr[1]
                elif substr[0] == "PORT":
                    self.PORT = int(substr[1])
                elif substr[0] == "BBDD_ADDR":
                    self.BBDD_ADDR = substr[1]
                elif substr[0] == "BBDD_USER":
                    self.BBDD_USER = substr[1]
                elif substr[0] == "BBDD_PASS":
                    self.BBDD_PASS = substr[1]
                elif substr[0] == "N_FILTROS":
                    self.N_FILTROS = int(substr[1])
                else:
                    print "Error al leer datos de configuracion"

            line = fd.readline()

        fd.close()

        # Creamos la instancia de la mib
	self.miBBDD = tools.BBDD(self.BBDD_ADDR, self.BBDD_USER, self.BBDD_PASS)
        self.mib = mib.mib(self.N_FILTROS, self.miBBDD)
	
	# Configuramos la alarma
	signal.signal(signal.SIGALRM, self.update)
	signal.alarm(10)

        # Creamos el agente
        self.transportDispatcher = AsynsockDispatcher()
        self.transportDispatcher.registerRecvCbFun(self.cbFun)

        self.transportDispatcher.registerTransport(
            udp.domainName, udp.UdpSocketTransport().openServerMode((self.IP_ADDR, self.PORT))
        )

        self.transportDispatcher.jobStarted(1)

        try:
            self.transportDispatcher.runDispatcher()
        except:
            self.transportDispatcher.closeDispatcher()
            raise


    def update(self, signum, frame):
	self.mib.rmon_filter.filtro.update()
	signal.alarm(10)


    # Comenzamos a procesar las peticiones
    def cbFun(self, transportDispatcher, transportDomain, transportAddress, wholeMsg):
        while wholeMsg:
            # Comprobamos la version del protocolo utilizada en el mensaje recivido
            msgVer = api.decodeMessageVersion(wholeMsg)
            if msgVer in api.protoModules:
                pMod = api.protoModules[msgVer]
            else:
                print('Unsupported SNMP version %s' % msgVer)
                return
            
            # Decodificamos el mensaje
            reqMsg, wholeMsg = decoder.decode(
                wholeMsg, asn1Spec=pMod.Message(),
                )
	                
            # Definimos el mensaje de respuesta y extraemos el PDU del mensaje
            rspMsg = pMod.apiMessage.getResponse(reqMsg)
            rspPDU = pMod.apiMessage.getPDU(rspMsg)
            reqPDU = pMod.apiMessage.getPDU(reqMsg)
            comunidad = pMod.apiMessage.getCommunity(reqMsg)
            varBinds = []; pendingErrors = []; almacen = []
            errorIndex = 0
            
            # GETNEXT PDU
            if reqPDU.isSameTypeWith(pMod.GetNextRequestPDU()):
                for oid, val in pMod.apiPDU.getVarBinds(reqPDU):		    		    
                    errorIndex = errorIndex + 1
                    exito_resp, type1_resp, oid_resp, type2_resp, val_resp = self.mib.getnext(oid, comunidad)
		    if exito_resp == 1:
                        # Tenemos la respuesta
                        varBinds = tools.formato(varBinds, oid_resp, val_resp, type2_resp, msgVer)
                    else:
                        # No tenemos la respuesta, enviamos varBind de error
                        varBinds.append((oid_resp, val))
                        pendingErrors.append(
                            (pMod.apiPDU.setEndOfMibError, errorIndex)
                            )
                        break  

            # GET PDU
            elif reqPDU.isSameTypeWith(pMod.GetRequestPDU()):
                
                for oid, val in pMod.apiPDU.getVarBinds(reqPDU):
                    errorIndex = errorIndex + 1
                    exito_resp, type1_resp, oid_resp, type2_resp, val_resp = self.mib.get(oid)
                    permisos = self.mib.comunidades.permiso(comunidad, oid)
                    if (exito_resp == 1) and ((permisos == 1) or (permisos == 3)):
                        # Tenemos la respuesta
                        varBinds = tools.formato(varBinds, oid_resp, val_resp, type2_resp, msgVer)
                    else:
                        # No tenemos la respuesta, enviamos varBind de error
                        varBinds.append((oid_resp, val))
                        pendingErrors.append(
                            (pMod.apiPDU.setNoSuchInstanceError, errorIndex)
                            )
                        break                

            # SET PDU
            elif reqPDU.isSameTypeWith(pMod.SetRequestPDU()):
                for oid, val in pMod.apiPDU.getVarBinds(reqPDU):
                    errorIndex = errorIndex + 1
                    permisos = self.mib.comunidades.permiso(comunidad, oid)
                    if (permisos == 2) or (permisos == 3):
                        # Si tengo permisos lanzo la peticion
                        almacen = self.mib.backup(oid,  almacen)
                        exito_resp, type1_resp, oid_resp, type2_resp, val_resp = self.mib.set(oid, val)
                        if (exito_resp == 1):
                            # Tenemos la respuesta
                            varBinds.append((oid, val))

                        else:
                            # No tenemos la respuesa, enviamos varBind de error
                            varBinds.append((oid, val))
                            pendingErrors.append(
                                (pMod.apiPDU.setNoSuchInstanceError, errorIndex)
                                )
                            self.mib.rollback(almacen)
                            break

                    else:
                        # No tenemos permiso, enviamos varBind de error
                        varBinds.append((oid, val))
                        pendingErrors.append(
                            (pMod.apiPDU.setNoSuchInstanceError, errorIndex)
                            )
                        self.mib.rollback(almacen)
                        break
                    
            # GetBulk PDU
            elif reqPDU.isSameTypeWith(pMod.GetBulkRequestPDU()):
                non_repeaters = pMod.apiBulkPDU.getNonRepeaters(reqPDU)
                max_repetitions = pMod.apiBulkPDU.getMaxRepetitions(reqPDU)
                for oid, val in pMod.apiPDU.getVarBinds(reqPDU):
                    errorIndex = errorIndex + 1
                    if errorIndex <= non_repeaters:
                        exito_resp, type1_resp, oid_resp, type2_resp, val_resp = self.mib.get(oid)
                        permisos = self.mib.comunidades.permiso(comunidad, oid_resp)
                        if (exito_resp == 1) and ((permisos == 1) or (permisos == 3)):
                        # Tenemos la respuesta
                            varBinds = tools.formato(varBinds, oid_resp, val_resp, type2_resp, msgVer)
                        else:
                            # No tenemos la respuesta, enviamos varBind de error
                            varBinds.append((oid_resp, val))
                            pendingErrors.append(
                                (pMod.apiPDU.setNoSuchInstanceError, errorIndex)
                                )
                            break
                        
                    else:
                        oid_resp = oid
                        for i in range(max_repetitions):
                            exito_resp, type1_resp, oid_resp, type2_resp, val_resp = self.mib.getnext(oid_resp)
                            if (exito_resp == 1):
                            # Tenemos la respuesta
                                varBinds = tools.formato(varBinds, oid_resp, val_resp, type2_resp, msgVer)
                            else:
                                # No tenemos la respuesta, enviamos varBind de error
                                varBinds.append((oid_resp, val_resp))
                                pendingErrors.append(
                                    (pMod.apiPDU.setNoSuchInstanceError, errorIndex)
                                    )
                                break
                    
            # Si el mensaje no pertenece a ninguno de los tipos soportados        
            else:
                pMod.apiPDU.setErrorStatus(rspPDU, 'genErr')

            # Añadimos los varBinds al mensaje
            pMod.apiPDU.setVarBinds(rspPDU, varBinds)
            
            # Introducimos los posible indices de error al PDU
            for f, i in pendingErrors:
                f(rspPDU, i)

            # Enviamos el mensaje    
            transportDispatcher.sendMessage(
                encoder.encode(rspMsg), transportDomain, transportAddress
                )
            
        return wholeMsg  




