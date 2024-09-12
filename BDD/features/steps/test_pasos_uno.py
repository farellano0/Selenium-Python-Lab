from behave import *
from Funciones import FuncionesGlobales

WAIT_TIME = 1

@given(u'Abriendo el navegador')
def step_impl(context):
    global driver, funcion
    funcion = FuncionesGlobales()
    funcion.init()
    funcion.navegar("https://demoqa.com/text-box")


@when(u'Cargando el nombre del "{user}"')
def step_impl(context, user):
    print(u'STEP: When Cargando el nombre del usuario')
    funcion.validar_texto("id", "userName", user, WAIT_TIME)


@then(u'Cargando su "{email}"')
def step_impl(context, email):
    print(u'STEP: Then Cargando su email')
    funcion.validar_texto("id", "userEmail", email, WAIT_TIME)


@then(u'Cargando su nueva "{dir}"')
def step_impl(context, dir):
    print(u'STEP: Then Cargandosu dirección')
    funcion.validar_texto("id", "currentAddress", dir, WAIT_TIME)
