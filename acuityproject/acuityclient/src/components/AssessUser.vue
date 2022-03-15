<template>
    <div class="assess">
        <main-header></main-header>
        <h1>{{$route.params.id}}</h1>

        <q-button @click="updateScore(1)" :disabled="score >= max" class="assess-control" theme="secondary" type="icon" icon="q-icon-triangle-up" circle></q-button>
        <p class="assess-counter">{{score}}</p>
        <q-button @click="updateScore(-1)" :disabled="score <= min" class="assess-control" theme="secondary" type="icon" icon="q-icon-triangle-down" circle></q-button>
    
        <p><q-button @click="send">Send</q-button></p>
    </div>
</template>

<script>
import MainHeader from './MainHeader.vue'
import axios from 'axios'
export default {
  components: { MainHeader },
    name: 'AssessUser',
    data() {
        return{
            score: 4,
            max: 5,
            min: 1,
        }
    },
    methods: {
        updateScore(n){
            this.score += n;
            if(this.score > this.max)
                this.score = this.max
            else if(this.score < this.min)
                this.score = this.min
        },
        send(){
            const data = {
                score: this.score,
            }

            axios.post('http://localhost:8000/api/assess/', data)
                .then(response => {
                    console.log(response)
                })
                .catch(error => {
                    console.log(error)
                })
        },
    },
}
</script>
