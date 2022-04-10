<template>
    <div class="assess h100">
        <main-header :isClose="true" :isFixed="true"></main-header>

        <div class="column">
            <div class='item h20'><h1>{{user.firstName+" "+user.lastName}}</h1></div>
            <div class="item h20 assess-counter">{{user.scoreMean.toFixed(1)}}</div>

            <div class="column item h60 comments-container">
                <p v-if="Object.keys(assess).length == 0">Nobody has judged him for now</p>
                <q-scrollbar theme="secondary" class="rounded-border w80">
                    <div class="w100 comment-box" v-for="a in assess" :key="a">
                        <p :class="{border: a.comment == ''}" class="title">
                            <q-button theme="link">{{a.from_user.first_name}} {{a.from_user.last_name}}</q-button> 

                            <label class="space-left accent-text">{{a.score}}</label>
                        </p>
                        <p v-if="a.comment != ''" class="comment">{{a.comment}}</p>
                    </div>
                </q-scrollbar>
            </div>
        </div>

    </div>
</template>

<script>
import axios from 'axios'
import MainHeader from './MainHeader.vue';
export default {
  components: { MainHeader},
    name: 'AssessUser',
    data() {
        return{
            user:{
                id: -1,
                firstName: '',
                lastName: '',
                email: '',
                scoreMean: -1,
            },
            assess: {},
        }
    },
    mounted(){
        this.getUserInfos()
    },
    methods: {
        getUserInfos(){
            axios.get(this.$router.routeApi('/users/' + this.$route.params.id + '/'))
                .then(response => {
                    console.log(response)
                    this.user.id = response.data.id
                    this.user.firstName = response.data.first_name
                    this.user.lastName = response.data.last_name
                    this.user.email = response.data.email
                    this.user.scoreMean = response.data.score_mean
                })
                .then(()=>{
                    this.getAssess()
                })
                .catch(error => {
                    let status = error.response.status;
                    if(status == 401)
                        this.$router.push("/log-in")
                    console.log(error)
                })
        },
        getAssess(){
            axios.get(this.$router.routeApi('/users/'+this.$route.params.id+ '/assess/'))
                .then(response => {
                    this.assess = response.data
                })
                .catch(error => {
                    let status = error.response.status;
                    if(status == 401)
                        this.$router.push("/log-in")
                    console.log(error)
                })
        }
    },
}
</script>
