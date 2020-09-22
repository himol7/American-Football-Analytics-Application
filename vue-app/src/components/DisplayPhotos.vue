<template>
  <div class ="card">
    <div v-if="isPhotoAvailable">
        <b-card  border-variant = "info" fluid>
            <b-row>
                <b-col cols="8">
                    <div v-b-scrollspy:scrollspy-nested >
                        <div>
                            <b-card-img left :src="selectedImg.link" class="selected-img"></b-card-img>
                        </div>
                    </div>
                </b-col>
                <b-col cols="4">
                    <b-navbar id="scrollspy-nested" class="flex-column" style="position:absolute; height:100%; overflow-y:auto">
                        <b-nav pills vertical>
                            <b-nav-item href="#item-1" v-for="photo in photos" :key="photo.id">
                                <b-img 
                                    thumbnail 
                                    :src="photo.link" 
                                    class="list-img"
                                    @click="changeImage(photo)"
                                   
                                ></b-img>
                            </b-nav-item>
                        </b-nav>
                    </b-navbar>
                </b-col>
            </b-row>
        </b-card>
    </div>
  </div>

</template>
<script>
import axios from "axios";
import { bus } from "@/event-bus";

export default {
  name: "DisplayPhotos",
  data() {
    return {
        photos: [],
        slide: 0,
        sliding: null,
        selectedImg: null
    };
  },
  computed: {
    isPhotoAvailable: function () {
      return this.photos.length > 0;
    },
  },
  created() {
    bus.$on("upload-success", () => {
      this.getReport();
    });
  },

  methods: {
    getReport() {
      axios
        .get("http://localhost:5000/analysis")
        .then((response) => {
          this.photos = response.data
          this.selectedImg = this.photos[0]
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    changeImage(photo) {
        this.selectedImg = photo
    }
  },
};
</script>
<style scoped>
.list-img {
    width: 100%;
    height: 100%;
}
.selected-img {
    width: 100%;
    height: 400px;
    
}
.card {
    width: 100%;
    height: 100%;

}
</style>
