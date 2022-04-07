<template>
    <div class="assess">
        <pop-up hidden size="200" :data="qrcode" />
        <close-header></close-header>
        <div class="column">
            <div class='item h20'><h1 theme="link">{{user.firstName+" "+user.lastName}}</h1>
                <pop-up @click="popUpClick()" :data="qrcode" size="25" />
            </div>
            <div class="item h20 assess-counter">{{user.scoreMean.toFixed(1)}}</div>

            <div class="column item h60 comments-container">

                <q-scrollbar theme="secondary" class="rounded-border w80">
                    <div class="w100 comment-box" v-for="a in assess" :key="a">
                        <p :class="{border: a.comment == ''}" class="title">
                            <q-button theme="link">{{a.fromUser.first_name}} {{a.fromUser.last_name}}</q-button> 
                            <label class="accent-text">{{a.score}}</label>
                        </p>
                        <p v-if="a.comment != ''" class="comment">{{a.comment}}</p>
                    </div>
                </q-scrollbar>
            </div>
        </div>

    </div>
</template>

<script>
import CloseHeader from './CloseHeader.vue'
import axios from 'axios'
import PopUp from './PopUp.vue'

export default {
  components: { CloseHeader, PopUp },
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
            axios.get(this.$router.routeApi('/myuser/'))
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
                    if (error.response.status == 401){
                        this.$router.push('/log-in')
                    }
                })
        },
        getAssess(){
            axios.get('http://localhost:8000/api/users/' + this.user.id + '/assess/')
                .then(response => {
                    this.assess = response.data
                    console.log(response)
                })
                .catch(error => {
                    console.log(error)
                })
        },
        popUpClick(){
            this.$swal({
                title: 'Your QRCode',
                html: this.fullQr,
            })
        }
    },
}
</script>
