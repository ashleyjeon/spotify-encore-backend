import React from 'react'; 


const LoginButton = () => {
    const handleLogin = () => {
        window.location.href = "https://spotify-encore.onrender.com/auth/login";
    }

    return (
        <button onClick={handleLogin}>
            Login with Spotify
        </button>
    );
}; 

export default LoginButton;