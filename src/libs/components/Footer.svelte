<script>
    import { Footer, FooterCopyright, FooterLink, FooterLinkGroup } from 'flowbite-svelte';
</script>

<Footer class="sticky top-[100vh] start-0 bottom-0 z-20 w-full border-t border-gray-200 bg-footer p-4 shadow-sm md:flex md:items-center md:justify-between md:p-6 dark:border-gray-600 dark:bg-gray-800">
  <FooterCopyright href="https://bytewhispersecurity.com/" by="Bytewhisper Security™" />
  <FooterLinkGroup class="mt-3 flex flex-wrap items-center text-sm text-gray-500 sm:mt-0 dark:text-gray-400">
    <FooterLink href="mailto://insecure-app@bytewhispersecurity.com">Support</FooterLink>
    <FooterLink href="/legal">Legal stuff</FooterLink>
  </FooterLinkGroup>
</Footer>