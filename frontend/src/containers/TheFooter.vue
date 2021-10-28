<template>
  <CFooter :fixed="false">
    <div class="left-side">
      <a href="https://vstorm.co/" target="_blank">
        &copy; {{ new Date().getFullYear() }} VSTORM All right reserved.
      </a>
    </div>
    <div class="mfs-auto right-side">
      <a href="https://www.linkedin.com/company/vstormco/" target="_blank"
        ><CIcon name="cib-linkedin"
      /></a>
      <a href="https://www.facebook.com/vstormco/" target="_blank"
        ><CIcon name="cib-facebook"
      /></a>
      <a href="https://dribbble.com/vstorm" target="_blank"><CIcon name="cib-dribbble" /></a>
    </div>
  </CFooter>
</template>

<script>
export default {
  name: "TheFooter",
};
</script>


<style scoped>
a {
  color: #3a3a3a;
  text-decoration: none;
  font-weight: bold;
}
.right-side a {
  padding-right: 20px;
}
</style>