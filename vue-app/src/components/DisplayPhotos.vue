<template>
    <div id = "app">
        "qazxsw"
        <img :src= "data" >
        "qwerty"
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'DisplayPhotos',
    data() {
        return{
            data: null
        }
    },
    beforeMount(){
        this.mounted()
    },
    methods: {
        mounted(){
            axios.get('http://localhost:5000/analysis')
            .then((response) =>{
                //let b64Response = btoa(unescape(encodeURIComponent(response.data)))
                this.data = response.data


            })
            .catch(function (error){
                console.log(error)
            })
        }
    }
}
</script>