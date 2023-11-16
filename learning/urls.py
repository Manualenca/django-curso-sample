from django.urls import path, register_converter
from . import views
from . import converters

register_converter(converters.DateRangeConverter, "daterange")


urlpatterns = [
    path("cursos/", views.list_cursos, name="list_cursos"),
    path("cursos_eliminados/", views.list_cursos_eliminados, name="list_cursos_eliminados"),
    path("cursos/<int:curso_id>/", views.detail_curso, name="detail_curso"),
    path("cursos/actualizar/<int:curso_id>/", views.update_curso, name="update_curso"),
    path("cursos/eliminar/<int:curso_id>/", views.delete_curso, name="delete_curso"),
    path("cursos/ocultar/<int:curso_id>/", views.hide_curso, name="hide_curso"),
    path("cursos/mostrar/<int:curso_id>/", views.restore_curso, name="show_curso"),
    path("cursos/crear", views.create_curso, name="create_curso"),
    path("estudiantes/crear", views.create_estudiante, name="create_estudiante"),
    path("estudiantes/", views.list_estudiantes, name="list_estudiantes"),
    path("inscripcion/", views.inscripcion_por_nombre, name="inscribir"), # original es views.inscripcion
    path(
        "estudiantes/<int:estudiante_id>/cursos/",
        views.estudiante_cursos,
        name="estudiante_cursos",
    ),
    path("inscripciones/", views.list_inscripciones, name="list_inscripciones"),
    path(
        "cursos/<int:curso_id>/estudiantes/",
        views.curso_estudiantes,
        name="curso_estudiantes",
    ),
    path(
        "cursos/<daterange:date_range>/",
        views.cursos_por_fecha,
        name="cursos-por-fecha",
    ),
]
