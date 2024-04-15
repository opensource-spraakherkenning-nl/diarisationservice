from diarisationservice import diarisationservice
import clam.clamservice
application = clam.clamservice.run_wsgi(diarisationservice)