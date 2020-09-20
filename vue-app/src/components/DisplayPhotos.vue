<template>
    <div>
        <div v-if="isPhotoAvailable">
            <img v-for="photo in photos" :key="photo.id" :src="photo.link" />
        </div>
    </div>
</template>


<script>
// import axios from 'axios'
import { bus } from '@/event-bus'

export default {
    name: 'DisplayPhotos',
    data() {
        return{
            mainProps: {
                center: true,
                fluidGrow: true,
                blank: true,
                blankColor: '#bbb',
                width: 600,
                heigh1t: 400,
                class1: 'my-5'
            },
            photos: []
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
            this.photos.push({"id": 1,"link": "https://picsum.photos/250/250/?image=54"})
            this.photos.push({"id": 2,"link": "https://picsum.photos/250/250/?image=54"})
            this.photos.push({"id": 3,"link": "https://picsum.photos/250/250/?image=54"})
            this.photos.push({"id": 4,"link": "https://picsum.photos/250/250/?image=54"})
            this.photos.push({"id": 5,"link": "https://picsum.photos/250/250/?image=54"})
            this.photos.push({"id": 6,"link": "https://picsum.photos/250/250/?image=54"})
            
        //     axios.get('http://localhost:5000/analysis')
        //     .then((response) =>{
        //         this.photos = response.data
        //     })
        //     .catch(function (error){
        //         console.log(error)
        //     })
        }
    }
}
</script>