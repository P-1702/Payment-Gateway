from django.shortcuts import render
from .forms import PaymentForm
import razorpay
from .models import Payment

cost_per_package= 35


def coffee_payment(request):
    if request.method == "POST":
        name = request.POST.get('name')
        quantity = int(request.POST.get('number_of_packages')) 
        instagram = request.POST.get('instagram')

        # create Razorpay client
        client = razorpay.Client(auth=('rzp_test_hxWUQLS6ueDYFo', 'egVyowmcvxIyOeXrWNqcdFeJ'))

        # create order
        response_payment = client.order.create(dict(amount=quantity*cost_per_package*100,
                                                    currency='INR')
                                               )

        order_id = response_payment['id']
        order_status = response_payment['status']

        if order_status == 'created':
            user_pay= Payment(
                name=name,
                amount=quantity*cost_per_package,
                order_id=order_id,
                instagram=instagram
            )
            user_pay.save()
            response_payment['name'] = name

            form = PaymentForm(request.POST or None)
            return render(request, 'coffee_payment.html', {'form': form, 'payment': response_payment})

    form = PaymentForm()
    return render(request, 'coffee_payment.html', {'form': form})


def payment_status(request):
    response = request.POST
    params_dict = {
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_signature': response['razorpay_signature']
    }

    # client instance
    client = razorpay.Client(auth=('rzp_test_hxWUQLS6ueDYFo', 'egVyowmcvxIyOeXrWNqcdFeJ'))

    try:
        status = client.utility.verify_payment_signature(params_dict)
        user_pay = Payment.objects.get(order_id=response['razorpay_order_id'])
        user_pay.razorpay_payment_id = response['razorpay_payment_id']
        user_pay.paid = True
        user_pay.save()
        return render(request, 'payment_status.html', {'status': True})
    except:
        return render(request, 'payment_status.html', {'status': False})
