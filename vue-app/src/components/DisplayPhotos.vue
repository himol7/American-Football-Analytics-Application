<template>
  <div class = "d-flex align-items-stretch">
    
    
    <div v-if="isPhotoAvailable">
        <b-carousel 
            id="carousel-1"
            v-model="slide"
            :interval="4000"
            controls
            indicators
            background="#ababab"
            img-width = "500"
            img-height = "00"
            style="text-shadow: 1px 1px 2px #333;"
            @sliding-start="onSlideStart"
            @sliding-end="onSlideEnd"
            v-bind="mainProps"
        >
          <b-carousel-slide caption="First slide" :img-src="photo.link" indicator = 'hover' v-for="photo in photos" :key="photo.id" ></b-carousel-slide>
        
        </b-carousel>
    </div>
    <p class="mt-4">
      Slide #: {{ slide }}<br>
      Sliding: {{ sliding }}
    </p>
    </div>
        
   <!-- <img v-for="photo in photos" :key="photo.id" :src="photo.link" /> -->
</template>
<script>
//import axios from 'axios'
import { bus } from '@/event-bus'

export default {
    name: 'DisplayPhotos',
    data() {
        return{
            
            photos: [],
            slide: 0,
            sliding: null
        }
    },
    computed: {
        isPhotoAvailable: function() {
            return this.photos.length > 0
        }
    },
    created() {
        bus.$on('upload-success', () => {
            this.getReport()
        })
    },

    methods: {
        getReport() {     
            this.photos.push({"id": 1,"link": "https://picsum.photos/500/300/?image=50"})
            this.photos.push({"id": 2,"link": "https://picsum.photos/400/650/?image=54"})
            this.photos.push({"id": 3,"link": "https://picsum.photos/250/250/?image=54"})
            this.photos.push({"id": 4,"link": "https://picsum.photos/250/250/?image=54"})
            this.photos.push({"id": 5,"link": "https://picsum.photos/250/250/?image=54"})
            this.photos.push({"id": 6,"link": "https://picsum.photos/250/250/?image=54"})
                        // axios.get('http://localhost:5000/analysis')
            // .then((response) =>{
            //     this.photos = response.data
            // })
            // .catch(function (error){
            //     console.log(error)
            // })
        }
    }
}
</script>
<style scoped>
.carousel {
    align-items: center;
    background-color: #666;
    color: #999; 
    display: flex;
    font-size: 1.5rem;
    justify-content: center;
    min-height: 10rem;

}
</style>
