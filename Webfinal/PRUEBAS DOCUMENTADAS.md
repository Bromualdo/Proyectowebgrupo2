# AppControlStock_Pozzi_Prinsich_Barderi

1) Al crear el registro de usuario, mediante el uso de la clase UserCreationForm, se lograba un usuario con 3 campos: usuario, contraseña y confirmación. Si bien nuestra aplicación se caracteriza por el hecho de ser lo más amigable e intuitiva, necesitábamos un campo más: correo electrónico. Y que los campos se pudieran customizar a efectos de que sea compatible con el estilo de la página. En consecuencia, investigamos y decidimos, primeramente, agregar el campo correo electrónico, mediante su añadimiento a la clase Meta.  Con ello logramos el campo faltante.  Luego, se modificaron los atributos de la clase UserCreationForm, a efectos de agregarle un widget que permita otorgarle estilo a los campos creados.  Finalmente,  se otorgó el estilo buscado.

2) Cuando decidimos que los usuarios de nuestra aplicación iban a tener una jerarquía (y que la jerarquía más alta pudiera crear usuarios de jerarquía más baja) nos dimos cuenta que faltaba un campo más en el formulario de registro. Y que, en dicho campo, tenía que existir la posibilidad de elegir uno de los 3 rangos de usuarios que habíamos definido. Nuevamente, lo agregamos como campo nuevo del User de la clase Meta y les otorgamos los permisos pertinentes según cada clase de usuario.

3) No lográbamos hacer que el login funcione, arrojaba un error que crasheaba la aplicación. Después de varios intentos, nos dimos cuenta que en el contexto que le estábamos pasando al template, le envíabamos el value, en vez de la key. Es decir, enviábamos el nombre del formulario creado, en lugar del nombre del contexto. Consignamos el nombre correcto y funcionó adecuadamente. Consideramos en ese momento adjudicar el mismo nombre a la key y al value para evitar errores u olvidos en el futuro, pero lo descartamos por cuestiones particulares de aprendizaje (error y comprensión)

4) Al realizar el formulario de registros , se nos ocurrio la idea de crear 3 grupos de jerarquias (Administrador,Responsable y Usuario).
Leyendo la documentacion logramos entender que el modelo User   mantiene una relacion de muchos a muchos con Groups bajo la instruccion User.groups mediante la tabla puente "auth_user_groups"
al generar el formulario  de registro (heredado del UserCreationForm) y definirle los campos a mostrar (incluido el groups  que se incluye bajo un forms.Modelchoicefield (queryset=Group.objects.all(), required=True) para que muestre todos los valores dentro del groups, procedimos al generar la funcion de registro en el views.py (hasta este punto solo muestra los grupos pero no lo asigna).
Aca nos encontramos con el problema de que, al momento de asignar los valores en su tabla puente esta nos daba valores repetidos siendo:
 nombre_usuario=formulario_registro_usuario.cleaned_data["username"] <-usuario creado en el formulario
 nombre_grupo=formulario_registro_usuario.cleaned_data["group"] <-grupo asignado en el formulario
 formulario_registro_usuario.save()<- se salva el registro en sus respectivas tablas
 nuevo_usuario=User.objects.get(username=nombre_usuario)<- obtención de ese nuevo usuario 
asigno_grupo=Group.objects.get(name=nombre_grupo)<-obtencion del grupo del formulario
 nuevo_usuario.groups.add(nuevo_usuario.id,asigno_grupo.id)<-- escritura de dichos valores en la tabla puente
Al realizar mas de una creación de usuario nos daba errores de foreign key (constraint) , porque nosotros no teníamos en cuenta que conceptualmente nuevo_usuario.groups.add ya tenia en cuenta no solo la primary key de la tabla puente , sino tambien el id del usuario.
Por lo que esta falla se logro solucionar despues de realizar la creación de muchos grupos y darnos cuenta de que en la base nos estaba  grabando siempre dos valores en dicha tabla puente  , por lo que simplemente en la instrucción eliminamos “el nuevo_usuario.id” dejango solo el “asigno_grupo.id” como única instruccion

   

