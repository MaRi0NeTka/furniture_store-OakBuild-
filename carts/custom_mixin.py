from django.template.loader import render_to_string
from django.urls import reverse
from carts.models import Cart
from carts.utils import get_user_carts


class CartMixin:
    def get_carts(self, request, product=None, cart_id=None):
        if request.user.is_authenticated:
            query_dict = {'user': request.user}
        else:
            query_dict = {'session_key': request.session.session_key}
        if product:
            query_dict['product'] = product
        if cart_id:
            query_dict['id'] = cart_id
            
        return Cart.objects.filter(**query_dict).first()
    

    def render_cart_items(self, request):
        user_carts = get_user_carts(request)
        context = {'carts': user_carts}

        referer = request.META.get('HTTP_REFERER')
        if reverse('orders:create_order') in referer:
            context['order'] = True
        return render_to_string('carts/includes/include_cart.html', context, request=request)
