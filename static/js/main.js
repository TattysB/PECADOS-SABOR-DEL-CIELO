// Interactividad principal de la landing page de Pecados Sabor del Cielo
document.addEventListener("DOMContentLoaded", () => {
    const navbar = document.getElementById("site-navbar");
    const navToggle = document.getElementById("nav-toggle");
    const primaryNav = document.getElementById("primary-nav");
    const cartCountEl = document.getElementById("cart-count");
    const toastEl = document.getElementById("site-toast");
    const newsletterForm = document.getElementById("newsletter-form");
    const newsletterFeedback = document.getElementById("newsletter-feedback");

    // 1. Transición de navbar transparente a sólida al hacer scroll en la landing.
    const updateNavbarState = () => {
        if (!navbar) return;
        navbar.classList.toggle("is-scrolled", window.scrollY > 36);
    };
    updateNavbarState();
    window.addEventListener("scroll", updateNavbarState, { passive: true });

    // 2. Menú móvil accesible.
    if (navToggle && primaryNav) {
        navToggle.addEventListener("click", () => {
            const isOpen = primaryNav.classList.toggle("is-open");
            navToggle.setAttribute("aria-expanded", String(isOpen));
        });

        primaryNav.querySelectorAll("a").forEach((link) => {
            link.addEventListener("click", () => {
                primaryNav.classList.remove("is-open");
                navToggle.setAttribute("aria-expanded", "false");
            });
        });
    }

    // 3. Notificación toast reutilizable.
    let toastTimer = null;
    const showToast = (message) => {
        if (!toastEl) return;
        toastEl.textContent = message;
        toastEl.classList.add("is-visible");
        clearTimeout(toastTimer);
        toastTimer = setTimeout(() => {
            toastEl.classList.remove("is-visible");
        }, 2800);
    };

    // 4. Contador interactivo temporal para los botones "+" de favoritos.
    let itemCount = 0;
    document.querySelectorAll("[data-add-item]").forEach((button) => {
        button.addEventListener("click", () => {
            const itemName = button.getAttribute("data-add-item") || "Producto";
            itemCount += 1;
            if (cartCountEl) {
                cartCountEl.textContent = String(itemCount);
                cartCountEl.classList.add("is-visible");
            }
            showToast(`"${itemName}" agregado a tu selección.`);
        });
    });

    // 5. Validación básica del formulario de boletín en el footer.
    if (newsletterForm && newsletterFeedback) {
        newsletterForm.addEventListener("submit", (event) => {
            event.preventDefault();
            const emailInput = newsletterForm.querySelector("input[type='email']");
            const email = emailInput ? emailInput.value.trim() : "";

            if (!email || !email.includes("@")) {
                newsletterFeedback.textContent = "Por favor ingresa un correo electrónico válido.";
                return;
            }

            newsletterFeedback.textContent = "¡Gracias por suscribirte! Muy pronto recibirás nuestras novedades.";
            newsletterForm.reset();
        });
    }
});
