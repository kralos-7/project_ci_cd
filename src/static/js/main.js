var intentos = 0;

function mostrarModal(titulo, idContenido) {
    var modal = document.getElementById('modal');
    modal.classList.remove('hidden');

    let contenidoModal = document.getElementById('cuerpoModal');
    let contenido = document.getElementById(idContenido).innerHTML;
    contenidoModal.innerHTML = '';
    contenidoModal.innerHTML = contenido;

    var modalTitulo = document.getElementById('tituloModal');
    modalTitulo.innerHTML = titulo;

    
    var toggleButton = document.querySelector('[data-modal-toggle="modal"]');
    if (toggleButton) {
        toggleButton.click();
    }
    
    
    

    

}
























function togglePasswordVisibility(passwordId, iconId) {
    const passwordInput = document.getElementById(passwordId);
    const eyeIcon = document.getElementById(iconId);

    const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordInput.setAttribute('type', type);

    // Cambiar dinámicamente el ícono del ojo
    if (type === 'password') {
        eyeIcon.src = 'static/images/eye-close.svg';
    } else {
        eyeIcon.src = 'static/images/eye-open.svg';
    }
}




/**
 * Permite navegar entre las pestañas "Iniciar Sesión" y "Registrarse". 
 * Al seleccionar una pestaña se muestra su contenido. 
 * @param {*} pestanaId 
 */
function cambiarPestana(pestanaId) {
    document.querySelectorAll('.tab-content').forEach(function (pestana) {
        pestana.classList.add('hidden'); 
    });
    document.getElementById(pestanaId).classList.remove('hidden');
}

function resaltarTab(idBotonTab) {
    var botonSeleccionado = document.getElementById(idBotonTab);

    document.querySelectorAll('[role="tab"]').forEach(function (boton) {
        boton.classList.remove('text-blue-600', 'dark:text-blue-500', 'border-blue-600', 'dark:border-blue-500', 'hover:border-blue-600', 'hover:text-blue-600', 'hover:border-gray-300', 'dark:hover:text-gray-300');
        boton.classList.remove('inline-block', 'border-b-2', 'rounded-t-lg', 'border-gray-300', 'dark:hover:text-gray-300', 'dark:border-transparent', 'text-gray-500', 'dark:text-gray-400', 'border-gray-100', 'dark:border-gray-700');
        boton.setAttribute('aria-selected', 'false');
        boton.classList.add('hover:border-gray-300', 'dark:hover:text-gray-300');
    });

    // Agregar clases de estilo cuando el botón está seleccionado
    botonSeleccionado.setAttribute('aria-selected', 'true');
    botonSeleccionado.classList.add('text-blue-600', 'dark:text-blue-500', 'border-blue-600', 'dark:border-blue-500');
    botonSeleccionado.classList.add('inline-block', 'border-b-2', 'rounded-t-lg');

    // Agregar clases de estilo específicas para el estado de hover
    botonSeleccionado.classList.add('hover:border-blue-600', 'hover:text-blue-600');
    botonSeleccionado.classList.remove('hover:border-gray-300', 'dark:hover:text-gray-300');
    

    // Agregar estilos de hover para la pestaña "Registrarse"
    // botonSeleccionado.classList.add('hover:border-gray-300', 'dark:hover:text-gray-300');
}

// function eliminarResaltado(){
//     pestana.setAttribute('aria-selected', 'false');
//     pestana.classList.add('inline-block', 'p-4', 'border-b-2', 'rounded-t-lg', 'dark:border-transparent', 'text-gray-500', 'hover:text-gray-600', 'dark:text-gray-400', 'border-gray-100', 'hover:border-gray-300', 'dark:border-gray-700', 'dark:hover:text-gray-300');
// }








document.getElementById('btnRecuperarPassword').addEventListener('click', function () {
    // mostrarModal("Recuperar contraseña", 'formForwotPassword')
    
});
