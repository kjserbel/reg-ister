from django.db import models
from django.contrib.auth.models import User

RC = 'Representante de Casilla' 
RG = 'Representante General'
MV = 'Movilizador'
SP = 'Simpatizante'

puesto_status = [
    (RC, 'Representante de Casilla'),
    (RG, 'Representante General'),
    (MV, 'Movilizador'),
    (SP, 'Simpatizante')
    ]


VA='Vasti Arana'
IBP='Isrrael y Profe'
OC='Omar Castellanos'
EC='Esther Castellanos'
CE='Cesar'
BE='Bere'
CL='Caleb Lupian'
ALO='Alonso'
AL='Abner Lopez'
ED='Edgar'
IS='Isai'
DP='Don Peter'
AD='Adin'


coordinador_status = [
    (VA, 'Vasti Arana'),
    (IBP, 'Israel y Profe'),
    (OC, 'Omar Castellanos'),
    (EC, 'Esther Castellanos'),
    (CE, 'Cesar'),
    (BE, 'Bere'),
    (CL, 'Caleb Lupian'),
    (ALO, 'Alonso'),
    (AL, 'Abner Lopez'),
    (ED, 'Edgar'),
    (IS, 'Isai'),
    (DP, 'Don Peter'),
    (AD, 'Adin')
    ]


GDL='Guadalajara'


municipio_status = [
    (GDL, 'Guadalajara')
    ]

JAL='Jalisco'

estado_status = [
    (JAL, 'Jalisco')
    ]

seccion_status = [
    (1218, '1218'),
    (1219, '1219'),
    (1220, '1220'),
    (1221, '1221'),
    (1213, '1213'),
    (1214, '1214'),
    (1215, '1215'),
    (1208, '1208'),
    (1207, '1207'),
    (1206, '1206'),
    (1204, '1204'),
    (1205, '1205'),
    (1192, '1192'),
    (1216, '1216'),
    (1217, '1217'),
    (1252, '1252'),
    (1250, '1250'),
    (1251, '1251'),
    (1249, '1249'),
    (1255, '1255'),
    (709, '0709'),
    (710, '0710'),
    (711, '0711'),
    (712, '0712'),
    (713, '0713'),
    (714, '0714'),
    (715, '0715'),
    (716, '0716'),
    (717, '0717'),
    (718, '0718'),
    (719, '0719'),
    (720, '0720'),
    (653, '0653'),
    (641, '0641'),
    (642, '0642'),
    (643, '0643'),
    (644, '0644'),
    (645, '0645'),
    (646, '0646'),
    (647, '0647'),
    (648, '0648'),
    (649, '0649'),
    (650, '0650'),
    (651, '0651'),
    (652, '0652'),
    (653, '0653'),
    (654, '0654'),
    (655, '0655'),
    (656, '0656'),
    (1334, '1334'),
    (1335, '1335'),
    (1331, '1331'),
    (1332, '1332')   
    ]

age = [
    (18, '18'),
    (19, '19'),
    (20, '20'),
    (21, '21'),
    (22, '22'),
    (23, '23'),
    (24, '24'),
    (25, '25'),
    (26, '26'),
    (27, '27'),
    (28, '28'),
    (29, '29'),
    (30, '30'),
    (31, '31'),
    (32, '32'),
    (33, '33'),
    (34, '34'),
    (35, '35'),
    (36, '36'),
    (37, '37'),
    (38, '38'),
    (39, '39'),
    (40, '40'),
    (41, '41'),
    (42, '42'),
    (43, '43'),
    (44, '44'),
    (45, '45'),
    (46, '46'),
    (47, '47'),
    (48, '48'),
    (49, '49'),
    (50, '50'),
    (51, '51'),
    (52, '52'),
    (53, '53'),
    (54, '54'),
    (55, '55'),
    (56, '56'),
    (57, '57'),
    (58, '58'),
    (59, '59'),
    (60, '60'),
    (61, '61'),
    (62, '62'),
    (63, '63'),
    (64, '64'),
    (65, '65'),
    (66, '66'),
    (67, '67'),
    (68, '68'),
    (69, '69'),
    (70, '70'),
    (71, '71'),
    (72, '72'),
    (73, '73'),
    (74, '74'),
    (75, '75')
    ]

# Create your models here.
class Task(models.Model):
    participacion = models.CharField(max_length=100, null=False, blank=False, choices=puesto_status)
    nombre_completo = models.CharField(max_length=150)
    edad = models.IntegerField(null= False, blank=False, choices=age, default=age, help_text = 'Selecciona tu Edad')
    calle_y_numero = models.CharField(max_length=250)
    masculino = models.BooleanField(default=False)
    femenino = models.BooleanField(default=False)
    colonia = models.CharField(max_length=200)
    c_p = models.CharField('C.P', max_length=250)
    municipio = models.CharField(max_length=250, null=False, blank=False, choices=municipio_status, default=None)
    estado = models.CharField(max_length=250, null=False, blank=False, choices=estado_status, default= None)
    num_seccion = models.IntegerField('Nº de Seccion', null=False, blank=False, choices=seccion_status, help_text='Selecciona una Seccion' )   
    num_casilla = models.CharField('Nº de Casilla',max_length=250, blank=True, help_text='Ingresa Num de Casilla',)
    nombre_enlace = models.CharField(max_length=250, null=False, blank=False, choices=coordinador_status, help_text='Selecciona tu Coordinador',)
    description = models.TextField('Comentarios',blank=True, default= 'Ingrese sus Comentarios (Opcional)')
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField('Fecha',null=True, help_text='Ejemplo: yyyy-mm-dd')
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.participacion + self.nombre_completo + ' - by ' + self.user.username