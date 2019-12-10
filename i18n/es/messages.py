class BaseBrowserConstants():
    BROWSERNOTEXIST = (
        "Por favor, ingresar un navegador en el archivo configuración"
    )
    OPENBROWSER = "Se ha abierto el navegador {}."
    SETURL = "Se ha abierto la url: {}"
    MAXIMIZE = "Se ha maximizado la ventana."
    NEWTAB = "Se ha abierto una nueva ventana con la url: {}."
    TAB_CHANGE_ERROR = "No existe una ventana en la posicion {}."
    TAB_CHANGE = (
        "Se modifica la ventana activa por la que se encuentra en la "
        "posicion {}."
    )
    CLOSE_TAB = "Se cierra la ventana activa."
    CLOSE_BROWSER = "Se cierra el navegador."


class BaseElementConstants():
    ELEMENT_NOT_VISIBLE = "El elemento {} no es visible."
    CLEAR_ELEMENT = "Se borra el contenido del elemento {}."
    WRITE_ELEMENT = "Se escribe el texto '{0}' en el elemento {1}"
    CLICK_ELEMENT = "Se hace click sobre el elemento {}."
    DOUBLE_CLICK_ELEMENT = "Se hace doble click sobre el elemento {}."
    SCROLL_ELEMENT = "Se desplaza hacia el elemento {}."
    HIGHLIGHT_ELEMENT = "Se resalta el elemento {}"
    REMOVE_HIGHLIGHT_ELEMENT = "Se quita lo resaltado al elemento {}."


class BasePageConstants():
    CAPTURE_IMAGE_ERROR = "La ruta de evidencias no está definido"
    COMPARE_TEXT_ERROR = (
        "El texto esperado '{0}', y el texto del elemento '{1}', "
        "son diferentes"
    )


class BaseRadioConstants():
    SELECT_OPTION = (
        "Se selecciona la opción con valor '{0}' dentro del conjunto de "
        "radiobutton del elemento {1}"
    )
    SELECT_OPTION_ERROR = (
        "El valor '{}' no se encuentra dentro de las opciones"
    )


class BaseSelectConstants():
    SELECT_BY_TEXT = (
        "Se selecciona la opción con el texto '{0}' "
        "del elemento select {1}"
    )
    SELECT_BY_TEXT_ERROR = (
        "Ninguna opción contiene el text '{0}' dentro del elemento {1}."
    )
    SELECT_BY_VALUE = (
        "Se selecciona la opción con el valor '{0}' del elemento select {1}"
    )
    SELECT_BY_INDEX = (
        "Se selecciona la opción que se encuentra en la posición {0} "
        "del elemento select {1}"
    )
    SELECT_BY_INDEX_ERROR = (
        "El elemento select {1}, no tiene opción en la posición {0}"
    )
