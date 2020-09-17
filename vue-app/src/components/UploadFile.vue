<template>
  <div>
    <div v-if="currentFile" class="progress">
      <div
        class="progress-bar progress-bar-info progress-bar-striped"
        role="progressbar"
        :aria-valuenow="progress"
        aria-valuemin="0"
        aria-valuemax="100"
        :style="{ width: progress + '%' }"
      >
        {{ progress }}%
      </div>
    </div>

    <label class="btn btn-default">
      <input type="file" ref="file" v-on:change="selectFile" />
    </label>

    <button class="btn btn-success"  @click="upload">
      Upload
    </button>

    <div class="alert alert-light" role="alert">{{ message }}</div>

    <div class="card">
      <div class="card-header">List of Files</div>
      <ul class="list-group list-group-flush">
        <li
          class="list-group-item"
          v-for="(file, index) in fileInfos"
          :key="index"
        >
          <a :href="file.url">{{ file.name }}</a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
    
import http from "../http-common"
export default {

    name:'FileUpload',
    data() {
      return {
        selectedFiles :undefined,
        currentFile: undefined,
        progress: 0,
        message: "",

        fileInfos: []
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
          
          return http.post("/upload", formData, {
            headers: {
                "Content-Type": "multipart/form-data"
            }            
            })
          .then(response => {
              this.message = response.data.message;
              return this.message
          })
          .then(files => {
          this.fileInfos = files.data;
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
