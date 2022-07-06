import io
import gphoto2 as gp

from app.models.camera import Camera

from .camera import CameraController


class GphotoController(CameraController):
    @staticmethod
    def _get_gp_camera(camera: Camera) -> gp.Camera:
        port_info_list = gp.PortInfoList()
        port_info_list.load()
        abilities_list = gp.CameraAbilitiesList()
        abilities_list.load()
        camera_list = abilities_list.detect(port_info_list)
        gp_camera = gp.Camera()
        idx = port_info_list.lookup_path(camera.path)
        gp_camera.set_port_info(port_info_list[idx])
        idx = abilities_list.lookup_model(camera_list[0][0])
        gp_camera.set_abilities(abilities_list[idx])
        return gp_camera

    def photo(camera: Camera) -> io.BytesIO:
        gp_camera = GphotoController._get_gp_camera(camera)
        file_path = gp_camera.capture(gp.GP_CAPTURE_IMAGE)
        camera_file = gp_camera.file_get(
            file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL
        )
        gp_camera.exit()
        return io.BytesIO(camera_file.get_data_and_size())

    def preview(camera: Camera) -> io.BytesIO:
        gp_camera = GphotoController._get_gp_camera(camera)
        camera_file = gp.gp_camera_capture_preview(gp_camera)[1]
        gp_camera.exit()
        return io.BytesIO(camera_file.get_data_and_size())
