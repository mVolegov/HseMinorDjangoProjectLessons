from django.shortcuts import render

# http://localhost:8000/carWebsiteApp/home/


def def_url_elements(request):
    url_elements_list = request.path.split("/")

    print("url_elements_list: ", url_elements_list)
    print("last_url_element: ", url_elements_list[-2])

    return {"last_url_element": url_elements_list[-2]}


def home(request):
    last_url_element = def_url_elements(request)

    images_array = [
        {
            "img": "/CarWebSiteApp/images/home_img_1.jpg"
        },
        {
            "img": "/CarWebSiteApp/images/home_img_2.jpg"
        },
        {
            "img": "/CarWebSiteApp/images/home_img_3.jpg"
        },
        {
            "img": "/CarWebSiteApp/images/home_img_4.jpg"
        },
        {
            "img": "/CarWebSiteApp/images/home_img_5.jpg"
        },
        {
            "img": "/CarWebSiteApp/images/home_img_6.jpg"
        }
    ]

    content = {"urls": last_url_element, "img_array": images_array}

    return render(request, "carWebsiteApp/home.html", content)


def bmw_history(request):
    last_url_element = def_url_elements(request)

    images_array = [
        {
            "img": "/CarWebSiteApp/images/bmw_1.jpg"
        },
        {
            "img": "/CarWebSiteApp/images/bmw_2.jpg"
        },
        {
            "img": "/CarWebSiteApp/images/bmw_3.jpg"
        }
    ]

    content = {"urls": last_url_element, "img_array": images_array}

    return render(request, "carWebsiteApp/bmw_history.html", content)


def audi_history(request):
    last_url_element = def_url_elements(request)

    images_array = [
        {
            "img": "/CarWebSiteApp/images/audi_1.jpg"
        },
        {
            "img": "/CarWebSiteApp/images/audi_2.jpg"
        },
        {
            "img": "/CarWebSiteApp/images/audi_3.jpg"
        },
        {
            "img": "/CarWebSiteApp/images/audi_4.jpg"
        },
        {
            "img": "/CarWebSiteApp/images/audi_5.jpg"
        },
        {
            "img": "/CarWebSiteApp/images/audi_6.jpg"
        },
        {
            "img": "/CarWebSiteApp/images/audi_7.jpg"
        }
    ]

    content = {"urls": last_url_element, "img_array": images_array}

    return render(request, "carWebsiteApp/audi_history.html", content)


def mercedes_history(request):
    last_url_element = def_url_elements(request)

    images_array = [
        {
            "img": "/CarWebSiteApp/images/merc_1.jpg"
        },
        {
            "img": "/CarWebSiteApp/images/merc_2.jpg"
        },
        {
            "img": "/CarWebSiteApp/images/merc_3.jpg"
        },
        {
            "img": "/CarWebSiteApp/images/merc_4.jpg"
        },
        {
            "img": "/CarWebSiteApp/images/merc_5.jpg"
        },
        {
            "img": "/CarWebSiteApp/images/merc_6.jpg"
        }
    ]

    mercs_300_images_array = [
        {
            "img": "/CarWebSiteApp/images/merc_300_1.jpg"
        },
        {
            "img": "/CarWebSiteApp/images/merc_300_2.jpg"
        },
        {
            "img": "/CarWebSiteApp/images/merc_300_3.jpg"
        },
        {
            "img": "/CarWebSiteApp/images/merc_300_4.jpg"
        },
        {
            "img": "/CarWebSiteApp/images/merc_300_5.jpg"
        }
    ]

    mercs_w123_images_array = [
        {
            "img": "/CarWebSiteApp/images/merc_w123_1.jpg"
        },
        {
            "img": "/CarWebSiteApp/images/merc_w123_2.jpg"
        },
        {
            "img": "/CarWebSiteApp/images/merc_w123_3.jpg"
        },
        {
            "img": "/CarWebSiteApp/images/merc_w123_4.jpg"
        }
    ]

    content = {
        "urls": last_url_element,
        "img_array": images_array,
        "mercs_300_img_array": mercs_300_images_array,
        "merc_w123_img_array": mercs_w123_images_array
   }

    return render(request, "carWebsiteApp/mercedes_history.html", content)


def volkswagen_history(request):
    last_url_element = def_url_elements(request)

    images_array = [
        {
            "img": "/CarWebSiteApp/images/vw_1.jpg"
        },
        {
            "img": "/CarWebSiteApp/images/vw_2.jpg"
        },
        {
            "img": "/CarWebSiteApp/images/vw_3.jpg"
        },
        {
            "img": "/CarWebSiteApp/images/vw_4.jpg"
        },
        {
            "img": "/CarWebSiteApp/images/vw_5.jpg"
        },
        {
            "img": "/CarWebSiteApp/images/vw_6.jpg"
        }
    ]

    content = {
        "urls": last_url_element,
        "img_array": images_array
    }

    return render(request, "carWebsiteApp/volkswagen_history.html", content)


def edit_history_form(request):
    last_url_element = def_url_elements(request)

    return render(request, "carWebsiteApp/edit_history_form.html", last_url_element)


def calculate_loan_form(request):
    last_url_element = def_url_elements(request)

    return render(request, "carWebsiteApp/calculate_loan_form.html", last_url_element)
