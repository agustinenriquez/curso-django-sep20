from django import template


register = template.Library()


@register.simple_tag(takes_context=True)
def add_click_to_course_image(context):
    url = context['request'].path + "inscripcion"
    let_img = "let imagen_curso = document.querySelector(\'img[id=imagen-curso]\');"
    href = "imagen_curso.onclick = function(){ window.location.href = '" + url + "'}"
    return (f"{let_img}{href}")
