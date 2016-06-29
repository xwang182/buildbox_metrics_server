from rest_framework import filters
from rest_framework import generics

from buildbox_metrics.models import BuildTrain, Build, Deliverable
from buildbox_metrics.serializers import (BuildTrainSerializer,
                                          BuildSerializer,
                                          DeliverableSerializer)


class BuildTrainList(generics.ListCreateAPIView):
    queryset = BuildTrain.objects.all()
    serializer_class = BuildTrainSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('buildbox_train_key', 'name',
                     'product_name', 'codename', 'release_type')


class BuildTrainDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BuildTrain.objects.all()
    serializer_class = BuildTrainSerializer


class BuildList(generics.ListCreateAPIView):
    queryset = Build.objects.all()
    serializer_class = BuildSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('buildbox_build_key', 'train', 'natural_number', 'status')


class BuildDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Build.objects.all()
    serializer_class = BuildSerializer


class DeliverableList(generics.ListCreateAPIView):
    queryset = Deliverable.objects.all()
    serializer_class = DeliverableSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('buildbox_deliverable_key', 'build', 'deliv_type',
                     'variant', 'packaging_process', 'status',
                     'total_build_time', 'initial_processing_time',
                     'waiting_time', 'queued_time', 'running_time')


class DeliverableDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deliverable.objects.all()
    serializer_class = DeliverableSerializer
