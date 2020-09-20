<template>
  <div>
    <label class="btn btn-default">
      <input type="file" ref="file" v-on:change="selectFile" />
    </label>

    <button class="btn btn-success"  @click="upload">
      Upload
    </button>

    <div class="alert alert-light" role="alert">{{ message }}</div>

  </div>
</template>

<script>
    
import http from "@/http-common"
import { bus } from "@/event-bus"

export default {

    name:'FileUpload',
    data() {
      return {
        selectedFiles :undefined,
        currentFile: undefined,
        progress: 0,
        message: "",

      }
    },
    methods: {
     
      selectFile() {
          this.selectedFiles = this.$refs.file.files
      },
      upload() {
          this.progress = 0
          this.currentFile = this.selectedFiles.item(0)
          console.log(this.currentFile)
          let formData = new FormData()
          formData.append("file", this.currentFile)
          bus.$emit('upload-success')
          return http.post("/upload", formData, {
            headers: {
                "Content-Type": "multipart/form-data"
            }            
            })
          .then(response => {
              console.log("Success!")
              bus.$emit('upload-success')
              console.log(response.data)
          })
         .catch(() => {
          this.progress = 0;
          this.message = "Could not upload the file!";
          this.currentFile = undefined;
         });

      },
    
  }
      
}  
</script>
