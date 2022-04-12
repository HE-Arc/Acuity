<template>
    <div class="assess h100">
        <main-header :isClose="true" :isFixed="true"></main-header>

        <div class="column">
            <div class='item h20'><h1>{{user.firstName+" "+user.lastName}}</h1></div>
            <div class="item h20 assess-counter">{{user.scoreMean.toFixed(1)}}</div>

            <div class="column item h60 comments-container">
                <assess-list v-if="user.id!=-1" :userId="user.id"/>
            </div>
        </div>

    </div>
</template>

<script>
import axios from 'axios'
import MainHeader from './MainHeader.vue';
import AssessList from './AssessList.vue'
import { useNotify, NotifyType } from '@qvant/qui-max';
export default {
  components: { MainHeader, AssessList },
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
    beforeMount(){
        this.getUserInfos()
    },
    methods: {
        checkDangerosity(){
            const notify = useNotify()
            if(this.user.scoreMean <= 1.5)
                notify('Be careful, this person could be dangerous', {duration: 50000, type: NotifyType.WARNING,})
            else if(this.user.scoreMean < 3)
                notify('Be careful, this person could be bad company', {duration: 50000, type: NotifyType.WARNING,})
        },
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
                    this.checkDangerosity()
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
