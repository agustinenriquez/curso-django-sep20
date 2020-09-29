from django import template


register = template.Library()


@register.simple_tag(takes_context=True)
def add_click_to_course_image(context):
<<<<<<< HEAD
    url = context["request"].path
    let_img = "let imagen_curso = document.querySelector(\'img[id=imagen-curso]\');"
    href = "imagen_curso.onclick = function() { window.location.href = '" + url + "' }"
    return (f"{let_img}{href}")
=======
    url = context['request'].path + "inscripcion"
    let_img = "let imagen_curso = document.querySelector(\'img[id=imagen-curso]\');"
    href = "imagen_curso.onclick = function(){ window.location.href = '" + url + "'}"
    return (
        f"{let_img}"
        f"{href}"
        )
>>>>>>> dinamically setting href onclick img url
