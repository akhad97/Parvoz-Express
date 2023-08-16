import os
from datetime import datetime
from django.db.models import Sum, Q
from django.utils import timezone
from django.utils.text import slugify
from ..common.validations import CustomValidationError


def upload_images(instance, path):
    filename = os.path.basename(path)
    filename_without_extension, extension = os.path.splitext(filename.lower())
    timestamp = timezone.now().strftime("%Y-%m-%d.%H-%M-%S")
    filename = f"{slugify(filename_without_extension)}.{timestamp}{extension}"
    return os.path.join(path, filename)


def get_prepayment_percentage(model):
    try:
        total = model.objects.aggregate(total=Sum('total_amount'))['total'] or 0
        prepayment = model.objects.aggregate(prepayment=Sum('prepayment'))['prepayment'] or 0
        
        if total == 0:
            prepayment_percentage = 0
        else:
            prepayment_percentage = round((prepayment / total) * 100, 2)
        
        data = {
            'prepayment_percentage': prepayment_percentage,
            'total_cash': total,
            'prepayment_cash': prepayment,
        }
        return data
    except Exception as e:
        raise CustomValidationError(msg=e.args)


def get_remained_amount_percentage(model):
    try:
        total = model.objects.aggregate(total=Sum('total_amount'))['total'] or 0
        prepayment = model.objects.aggregate(prepayment=Sum('prepayment'))['prepayment'] or 0
        
        if total == 0:
            remained_amount_percentage = 0
            remained_cash = 0
        else:
            remained_amount_percentage = round(((total - prepayment) / total) * 100, 2)
            remained_cash = total - prepayment
        
        data = {
            'remained_amount_percentage': remained_amount_percentage,
            'remained_cash': remained_cash
        }
        return data
    except Exception as e:
        raise CustomValidationError(msg=e.args)


def get_unpaid_percentage(model):
    try:
        total = model.objects.aggregate(total=Sum('total_amount'))['total'] or 0
        prepayment = model.objects.aggregate(prepayment=Sum('prepayment'))['prepayment'] or 0
        
        if total == 0:
            unpaid_percentage = 0
        else:
            unpaid_percentage = round(((total - prepayment) / total) * 100, 2)
        
        return unpaid_percentage
    except Exception as e:
        raise CustomValidationError(msg=e.args)