<template>
    <div> 
        <div v-if="isPhotoAvailable">
            <img v-for="photo in photos" :key="photo.id" :src="photo.link" />
        </div>
        

    </div>
</template>


<script>
import axios from 'axios';

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
    beforeMount(){
        this.getReport()
    },
    methods: {
        getReport() {
            axios.get('http://localhost:5000/analysis')
            .then((response) =>{
                this.photos = response.data
            })
            .catch(function (error){
                console.log(error)
            })
        }
    }
}
</script>