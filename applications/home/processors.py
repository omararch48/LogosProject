from .models import HomeText


def home_dict(request):
    home_texts = HomeText.objects.filter(active='0')
    generated_styles = """
    """
    style_core_mosaic = """
    background-position: center/center;
    background-repeat:   no-repeat;
    background-size:     cover;    
    height:              100%;
    margin:              0;
    padding:             0;
    width:               50%;"""
    style_core_colors = """
    background-position: center/center;
    background-repeat:   no-repeat;
    background-size:     cover;    
    height:              100vh;
    margin:              2rem 0;
    padding:             0;
    width:               100%;"""
    for element in home_texts:
        if element.model == 'mosaic':
            img_one = '\u0027' + element.image_one + '\u0027'
            img_two = '\u0027' + element.image_two + '\u0027'
            generated_styles = generated_styles + f"""
.section-home-mosaic-{element.id}-one {'{'}
    background-image:    url({img_one});{style_core_mosaic}
{'}'}
        
.section-home-mosaic-{element.id}-two {'{'}
    background-image:    url({img_two});{style_core_mosaic}
{'}'}"""
        else:
            img_one = '\u0027' + element.image_one + '\u0027'
            generated_styles = generated_styles + f"""
.section-home-image-{element.id} {'{'}
    background-image:    url({img_one});{style_core_colors}
{'}'}"""
    with open('static/core/css/home-styles.css', 'w') as file_css:
        file_css.write(generated_styles)
    home_info = {
        'home_texts': home_texts,
        'generated_styles': generated_styles,
    }
    return home_info