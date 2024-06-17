from krita import DockWidgetFactory, DockWidgetFactoryBase
from .docker_example import docker_example


Application.addDockWidgetFactory(
    DockWidgetFactory("Docker Example",
                      DockWidgetFactoryBase.DockRight,
                      docker_example))
