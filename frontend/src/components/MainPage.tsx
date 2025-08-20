import { Box, TextField } from "@mui/material"
import { MdStart } from "react-icons/md"
import { IoStopCircleOutline } from "react-icons/io5"
import { useState } from "react"
import type { ChangeEvent, JSX } from "react"

function MainPage(): JSX.Element {
    const [isStart, setIsStart] = useState<boolean>(false)
    const [input, setInput] = useState<string>("")

    const changeStartStatus = () => {
        if(input != ""){
            setIsStart(!isStart)
            console.log(input)
            setInput("")
        }
    }

    const handleInput = (e: ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
        setInput(e.target.value)
    }
    return (
        <Box
            sx={{
                width: "100%",
                maxWidth: 700,
                borderRadius: 5,
                padding: 1,
                display: "flex",
                border: "1px solid #e0e0e0",
                boxShadow: "0 4px 20px rgba(0,0,0,0.08), 0 2px 8px rgba(0,0,0,0.06)",
                transition: "box-shadow 0.3s ease-in-out",
                "&:hover": {
                    boxShadow: "0 8px 32px rgba(0,0,0,0.12), 0 4px 16px rgba(0,0,0,0.08)",
                },
            }}
        >
            <div className="flex flex-row w-full gap-3 items-end">
                <TextField
                    fullWidth
                    placeholder="Ask Anything"
                    value={input}
                    id="fullWidth"
                    variant="outlined"
                    multiline
                    minRows={1}
                    maxRows={10}
                    onChange={handleInput}
                    sx={{
                        "& .MuiOutlinedInput-notchedOutline": { 
                            border: "none" 
                        },
                        "& .MuiInputLabel-root": {
                            display: "none"
                        },
                        "& .MuiInputLabel-shrink": {
                            display: "none"
                        }
                    }}
                />
                <button
                    onClick={changeStartStatus}
                    className="flex items-center justify-center p-2 text-2xl hover:bg-gray-100 rounded-lg transition-colors"
                >
                    {isStart ? <IoStopCircleOutline /> : <MdStart />}
                </button>
            </div>
        </Box>
    )
}

export default MainPage