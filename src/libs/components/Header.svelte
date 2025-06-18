<script>
    import { Navbar, NavBrand, NavHamburger, Button } from 'flowbite-svelte';
</script>

<header class="start-0 top-0 z-20 w-full border-b border-gray-200 bg-header shadow-sm flex items-center justify-between">
    <Navbar class="bg-header grow nav-format">
        <NavBrand href="/">
            <img class="bwlogo" src="/src/public/logo2.png" alt="Bytewhisper Security Logo" name="Bytewhisper Security" />
            <span class="self-center text-product-name font-semibold whitespace-nowrap dark:text-white">Insecure AI App</span>
        </NavBrand>
        <div class="flex items-center lg:order-2">
            <Button href="/" class="ml-2 button-normal">Home</Button>
            <Button href="/logs" class="ml-2 button-normal">Logs</Button>
            <NavHamburger />
        </div>
    </Navbar>
</header>