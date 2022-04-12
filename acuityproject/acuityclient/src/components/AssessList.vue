<template>

        <q-scrollbar theme="secondary" class="rounded-border w80">
            <p v-if="Object.keys(assess).length == 0">Nobody has judged you for now</p>
            <div class="w100 comment-box" v-for="a in assess" :key="a">
                <p :class="{border: a.comment == ''}" class="title">
                    <q-button @click="this.$router.push('/users/' + a.from_user.id)" theme="link">{{a.from_user.first_name}} {{a.from_user.last_name}}</q-button> 

                    <label class="space-left accent-text">{{a.score}}</label>
                </p>
                <p v-if="a.comment != ''" class="comment">{{a.comment}}</p>
            </div>
        </q-scrollbar>

</template>

<script>
import axios from 'axios'

export default {
  components: { },
    name: 'MyProfile',
    data() {
        return{
            assess: {},
        }
    },
    props: ['userId'],
    mounted(){
        this.getAssess()
    },
    methods: {
        getAssess(){
            axios.get(this.$router.routeApi("/users/" + this.userId + '/assess/'))
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
