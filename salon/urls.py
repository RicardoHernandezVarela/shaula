from django.urls import path, include
from django.views.generic.base import TemplateView
from salon.views import administrativo, estudiante, profesor

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('administrativo/', include(([
        path('', administrativo.GruposView.as_view(), name='grupos'),
        path('creargrupo/', administrativo.CrearGrupo.as_view(), name='crear-grupo'),
        path('grupo/<int:pk>/', administrativo.CursosView.as_view(), name='cursos'),
        # /grupo<int:pk>//
        path('grupo/<int:pk>/agregarcurso/', administrativo.crear_curso, name='crear-curso'),
        path('profesores/', administrativo.ProfesoresView.as_view(), name='profesores'),
        path('alumnos/', administrativo.AlumnosView.as_view(), name='alumnos'),
    ], 'salon'), namespace='adminis')),

    path('profesor/', include(([
        path('cursos/', profesor.ProfesorBoard.as_view(), name='board'),
        path('cursos/<int:pk>/', profesor.ver_secciones.as_view(), name='secciones'),
        path('cursos/seccion/<int:pk>', profesor.ver_actividades.as_view(), name='actividades'),
        path('cursos/seccion/calificarActividad/<int:pk>', profesor.calificar.as_view(), name='calificar'),
    ], 'salon'), namespace='profesor')),

]
