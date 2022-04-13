<template>
    <div class="assess h100">
        <main-header :isClose="true" :isFixed="true"></main-header>
        <div class="column">
            <div class='item h20'>
                <h1 @click="popUpClick()">{{user.firstName+" "+user.lastName}}</h1>
            </div>
            <div class="item h20 assess-counter">{{user.scoreMean.toFixed(1)}}</div>

            <div class="column item h50 comments-container">
                <assess-list v-if="user.id!=-1" :userId="user.id" :isYou="true"/>
            </div>
            <q-button @click="popUpClick()" class="item h10">MY QR</q-button>
        </div>

    </div>
</template>

<script>
import axios from 'axios'
import MainHeader from './MainHeader.vue'
import AssessList from './AssessList.vue'
import {useMessageBox} from '@qvant/qui-max';
import { defineAsyncComponent } from '@vue/runtime-core';

export default {
  components: { MainHeader, AssessList },
    name: 'MyProfile',
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
            qrcode: "",
        }
    },
    beforeMount(){
        this.getUserInfos()
    },
    methods: {
        getUserInfos(){
            axios.get(this.$router.routeApi('/users/myuser/'))
                .then(response => {
                    this.user.id = response.data.id
                    this.user.firstName = response.data.first_name
                    this.user.lastName = response.data.last_name
                    this.user.email = response.data.email
                    this.user.scoreMean = response.data.score_mean
                })
                .then(() => this.qrcode = location.origin + "/#/assess/" + this.user.id)
                .catch(error => {
                    let status = error.response.status;
                    if(status == 401)
                        this.$router.push("/log-in")
                    console.log(error)
                })
        },
        async popUpClick(){
            const messageBox = useMessageBox()
            await messageBox(
                {
                    component: defineAsyncComponent(()=> import('./PopUp.vue')),
                    props:{
                        data: this.qrcode,
                        size: 250
                    }
                }
            )
        }
    },
}
</script>
