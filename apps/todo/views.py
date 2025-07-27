import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.core.constants import TaskStatus
from .models import Task


class DashboardView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        tarefas = Task.objects.filter(user=request.user, is_deleted=False).order_by('-created_at')
        return render(
            request,
            'todo/dashboard.html',
            {
                'tarefas': tarefas,
                'tarefa_statuses': TaskStatus.choices,
            },
        )


@method_decorator(csrf_exempt, name='dispatch')
class CreateTaskView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=400)

        task = Task.objects.create(
            user=request.user,
            name=data.get('name'),
            description=data.get('description', ''),
            status=TaskStatus.TODO,
        )
        return JsonResponse({'status': 'ok', 'uuid': str(task.uuid)}, status=201)


@method_decorator(csrf_exempt, name='dispatch')
class UpdateStatusView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=400)

        try:
            task = Task.objects.get(uuid=data['uuid'], user=request.user)
            task.status = data['status']
            task.save(update_fields=['status'])
            return JsonResponse({'status': 'ok'})
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Tarefa não encontrada'}, status=404)
