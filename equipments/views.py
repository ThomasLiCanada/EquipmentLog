from django.shortcuts import render, redirect
from .forms import InputEquipmentForm, EquipmentSearchForm, InputEquipmentSuperuserForm
from .models import Equipment
import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.db.models import Q


# from datetime import datetime it is wrong


@login_required  # Add this decorator to ensure the user is authenticated
def input_equipment_view(request):
    context = {}
    if request.user.is_authenticated:

        if request.method == 'POST':
            form = InputEquipmentForm(request.POST, request.FILES)
            # form = InputEquipmentForm(request.POST, request.FILES, request=request)  # Pass the request
            # if form.is_valid():
            #     current_temperature = form.cleaned_data['temperature']
            #     cal_date = form.cleaned_data['cal_due_date']
            #     current_date = datetime.date.today()
            #     if cal_date > current_date:
            #         if current_temperature <= 23 and current_temperature >= 18:
            #             obj = form.save(commit=False)
            #             obj.save()
            #             return redirect('home_after_input')
            #         else:
            #             return redirect('pop_temperature')
            #     else:
            #         return redirect('pop_overdue')
            if form.is_valid():
                current_temperature = form.cleaned_data['temperature']
                cal_date = form.cleaned_data['cal_due_date']
                current_date = datetime.date.today()
                if cal_date >= current_date and current_temperature <= 23 and current_temperature >= 18:
                    obj = form.save(commit=False)
                    obj.save()
                    return redirect('home_after_input')
                else:
                    if cal_date < current_date and (current_temperature > 23 or current_temperature < 18):
                        return redirect('pop_overdue_temperature')
                    else:
                        if cal_date < current_date:
                            return redirect('pop_overdue')
                        if current_temperature > 23 or current_temperature < 18:
                            return redirect('pop_temperature')
                        else:
                            return redirect('pop_overdue')
        else:
            # Set the initial value for the "inspector" field when creating a new form instance
            form = InputEquipmentForm(initial={'inspector': request.user.username})

            # form = InputEquipmentForm()

        context['form'] = form

        return render(request, 'equipments/input_equipment_information.html', context)
    else:
        return redirect('login')


def home_view(request):
    equipments = Equipment.objects.all()
    reversed_equipments = list(reversed(equipments))
    return render(request, 'equipments/home.html', {'equipments': reversed_equipments})


def home_for_search_view(request):
    equipments = Equipment.objects.all()
    reversed_equipments = list(reversed(equipments))

    # Check if the form was submitted
    if request.method == 'GET':
        form = EquipmentSearchForm(request.GET)
        if form.is_valid():
            cr_number = form.cleaned_data['cr_number']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            current_date = datetime.date.today()

            # Build a filter using Q objects
            filter_params = Q()
            if cr_number:
                filter_params &= Q(CR_number=cr_number)
            if start_date:
                filter_params &= Q(date_of_use__range=(start_date, current_date))
            if start_date and end_date:
                filter_params &= Q(date_of_use__range=(start_date, end_date))

            # Apply filters to the queryset
            reversed_equipments = equipments.filter(filter_params)
            reversed_equipments = list(reversed(reversed_equipments))

    else:
        form = EquipmentSearchForm()
        reversed_equipments = equipments

    return render(request, 'equipments/home_for_search.html', {'equipments': reversed_equipments, 'form': form})


def home_view_for_correction(request):
    equipments = Equipment.objects.all()
    reversed_equipments = list(reversed(equipments))
    return render(request, 'equipments/home_for_correction.html', {'equipments': reversed_equipments})


def home_view_after_input(request):
    equipments = Equipment.objects.all()
    reversed_equipments = list(reversed(equipments))
    return render(request, 'equipments/list_all_first_row_special.html', {'equipments': reversed_equipments})


def popup_temperature_view(request):
    return render(request, 'equipments/pop_temperature.html')


def popup_overdue_view(request):
    return render(request, 'equipments/pop_over_due.html')


def popup_overdue_and_temperature_view(request):
    return render(request, 'equipments/pop_over_due_and_temperature.html')


def edit_equipment_view(request, equipment_id):
    context = {}
    if request.user.is_authenticated:
        equipment = get_object_or_404(Equipment,
                                      pk=equipment_id)  # Replace 'EquipmentModel' with your actual model name
        if request.method == 'POST':
            form = InputEquipmentSuperuserForm(request.POST, request.FILES, instance=equipment)
            if form.is_valid():
                # Update the equipment information
                form.save()
                return redirect('home')
        else:
            # Populate the form with existing equipment data
            form = InputEquipmentSuperuserForm(instance=equipment)

        context['form'] = form
        context['equipment'] = equipment
        return render(request, 'equipments/edit_equipment_information_superuser.html', context)
    else:
        return redirect('login')


def edit_last_equipment_view(request):
    context = {}
    if request.user.is_authenticated:
        # Get the last created or updated equipment record
        equipment = Equipment.objects.order_by('-id').first()  # Replace 'EquipmentModel' with your actual model name
        if equipment is not None:
            if request.method == 'POST':
                form = InputEquipmentForm(request.POST, request.FILES, instance=equipment)
                if form.is_valid():
                    # Update the equipment information
                    form.save()
                    return redirect('home_after_input')
            else:
                # Populate the form with existing equipment data
                form = InputEquipmentForm(instance=equipment)

            context['form'] = form
            context['equipment'] = equipment
            return render(request, 'equipments/edit_equipment_information.html', context)
        else:
            # Handle the case when no equipment records exist
            return redirect('input')  # You can define this URL as needed
    else:
        return redirect('login')
