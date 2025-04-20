import React, { useState } from 'react';
import axios from 'axios';

function Signup() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const signup = async () => {
    await axios.post('http://localhost:5000/signup', { email, password });
    alert("User Created!");
    window.location.href = '/';
  };

  return (
    <div>
      <h2>Signup</h2>
      <input value={email} onChange={e => setEmail(e.target.value)} placeholder="Email" />
      <input value={password} onChange={e => setPassword(e.target.value)} type="password" placeholder="Password" />
      <button onClick={signup}>Signup</button>
    </div>
  );
}

export default Signup;
