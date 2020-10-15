import http from "../http-common"

class UploadFileService{
    upload(file, onUploadProgress) {
        let formData = new FormData();

        formData.append("file", file);

        return http.post("/upload", formData, {
        headers: {
            "Content-Type": "multipart/form-data"
        },
        onUploadProgress
        }); 
    }

    getFiles() {
        return http.get("/analysis")
    }
}
export default new UploadFileService();