

def brands(request):
    from .models import Brand
    brand_list = Brand.objects.all()

    return {'brands': brand_list}
