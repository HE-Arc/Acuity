<template>
    <div class="qr-container">
        <qrcode-vue :size="size" :value="data" level="H" background="#edf1f4" foreground="#2c3e50"/>
    </div>
</template>

<script>
//import QrcodeScan from 'vue-material-design-icons/QrcodeScan.vue'
import QrcodeVue from 'qrcode.vue'
export default {
    components: { QrcodeVue },
    name: 'PopUp',
    data() {
        return{
        }
    },
    props: ['data', 'size']
}
</script>
