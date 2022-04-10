<template>
    <div class="assess h100">
        <pop-up hidden size="200" :data="qrcode" />
        <main-header :isClose="true" :isFixed="true"></main-header>
        <div class="column">
            <div class='item h20'>
                <h1 @click="popUpClick()">{{user.firstName+" "+user.lastName}}</h1>
                <!--<pop-up class="mini-qr" @click="popUpClick()" :data="qrcode" size="25" />-->
            </div>
            <div class="item h20 assess-counter">{{user.scoreMean.toFixed(1)}}</div>

            <div class="column item h50 comments-container">

                <q-scrollbar theme="secondary" class="rounded-border w80">
                    <p v-if="Object.keys(assess).length == 0">Nobody has judged you for now</p>
                    <div class="w100 comment-box" v-for="a in assess" :key="a">
                        <p :class="{border: a.comment == ''}" class="title">
                            <q-button theme="link">{{a.from_user.first_name}} {{a.from_user.last_name}}</q-button> 

                            <label class="space-left accent-text">{{a.score}}</label>
                        </p>
                        <p v-if="a.comment != ''" class="comment">{{a.comment}}</p>
                    </div>
                </q-scrollbar>
            </div>
            <q-button @click="popUpClick()" class="item h10">MY QR</q-button>
        </div>

    </div>
</template>

<script>
import axios from 'axios'
import PopUp from './PopUp.vue'
import MainHeader from './MainHeader.vue'
import {useMessageBox} from '@qvant/qui-max';
import { defineAsyncComponent } from '@vue/runtime-core';

export default {
  components: { PopUp, MainHeader },
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
            fullQr: "",
        }
    },
    mounted(){
        this.getUserInfos()
        this.fullQr = this.$el.children[0].children[0]
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
                .then(() => this.getAssess())
                .then(() => this.qrcode = "http://localhost:8081/#/assess/" + this.user.id)
                .catch(error => {
                    let status = error.response.status;
                    if(status == 401)
                        this.$router.push("/log-in")
                    console.log(error)
                })
        },
        getAssess(){
            axios.get('http://localhost:8000/api/users/' + this.user.id + '/assess/')
                .then(response => {
                    this.assess = response.data
                    console.log(response)
                })
                .catch(error => {
                    let status = error.response.status;
                    if(status == 401)
                        this.$router.push("/log-in")
                    console.log(error)
                })
        },
        async popUpClick(){
            const messageBox = useMessageBox()
            let r = await messageBox(
                {
                    component: defineAsyncComponent(()=> import('./PopUp.vue')),
                    props:{
                        data: this.qrcode,
                        size: 250
                    }
                }
            )
            console.log(r)
            // this.$swal.fire({
            //     title: 'Your QRCode',
            //     html: this.fullQr,
            // })
        }
    },
}
</script>
