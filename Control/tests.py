from django.test import TestCase

# Create your tests here.


# Con estos modelos podria crear un sitio web 
# donde pueda listar los pacientes, hacerles 
# un CRUD, ver la historia clinica agregada 
# a cada uno de los pacientes, y en otra pagina 
# pueda Listar las HistoriasClinicas y 
# hacerles un CRUD?

# <a
# 							href="{% url 'crear_historia_clinica'%}?paciente_id={{ paciente.id_paciente }}"
# 							>{{ paciente.nombre }}</a
# 						>

# <td>
# 						<form
# 							action="{% url 'ver_historia_clinica' historiaclinica.paciente.id_paciente %}"
# 							method="GET">
# 							<button type="submit">Ver Historia Clínica</button>
# 						</form>
# 					</td>