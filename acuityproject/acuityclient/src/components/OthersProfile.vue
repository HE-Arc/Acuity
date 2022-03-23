<template>
    <div class="assess">
        <close-header></close-header>

        <div class="column">
            <div class='item h20'><h1 theme="link">{{user.firstName+" "+user.lastName}}</h1></div>
            <div class="item h20 assess-counter">{{user.scoreMean}}</div>

            <div class="item h20"><q-button class='assess-send' @click="isCommenting=true">Continue</q-button></div>
        </div>

    </div>
</template>

<script>
import CloseHeader from './CloseHeader.vue'
import axios from 'axios'
export default {
  components: { CloseHeader },
    name: 'AssessUser',
    data() {
        return{
            user:{
                id: -1,
                firstName: '',
                lastName: '',
                email: '',
                scoreMean: -1,
            }
        }
    },
    mounted(){
        this.getUserInfos()
    },
    methods: {
        getUserInfos(){
            axios.get('http://localhost:8000/api/users/' + this.$route.params.id + '/')
                .then(response => {
                    this.user.id = response.data.id
                    this.user.firstName = response.data.first_name
                    this.user.lastName = response.data.last_name
                    this.user.email = response.data.email
                    this.user.scoreMean = response.data.score_mean
                })
                .catch(error => {
                    console.log(error)
                })
        },
        getAssess(){
            //axios.get('http://localhost:8000/api/assess/')
        }
    },
}
</script>
