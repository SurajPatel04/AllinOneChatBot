import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import { Button } from "@/components/ui/button"
import MainPage from './components/MainPage'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <MainPage/>
    </>
  )
}

export default App
