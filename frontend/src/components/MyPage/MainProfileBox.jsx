import {
    Box, Button, Typography,
    Modal,
    IconButton,
    Toolbar,
} from '@mui/material';
import QRBox from '../../components/MyPage/QRBox';
import CropFreeIcon from '@mui/icons-material/CropFree';
import CloseIcon from '@mui/icons-material/Close';
import React, {useState} from 'react';

const previewImg = "data:image/jpeg;base64,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";

const style = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: 400,
    height: 400,
    bgcolor: 'background.paper',
    borderRadius: '20px',
    boxShadow: 24,
    p: 4,
};

export default function MainProfileBox() {
    const [open, setOpen] = useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);

    return(
        <Box>
            <Box sx={{display: 'flex', justifyContent: 'center', flexDirection: 'column', alignItems: 'center'}}>
                <img src={previewImg}/>
                <Toolbar sx={{mt: '20px'}}>
                    <Typography>
                        doriMong
                    </Typography>
                    
                    <IconButton onClick={handleOpen} sx={{ml: '10px',display: 'flex', alignItems: 'flex-end'}}>
                        <CropFreeIcon/>
                    </IconButton>
                </Toolbar>

                <Button sx={{mt: '10px', backgroundColor: '#D9D9D9', color: '#000',
                  "&:hover": {backgroundColor: '#848484', color: '#BEBEBE'}}} >
                    친구 추가
                </Button>
            </Box>

            <Modal
                open={open}
                onClose={handleClose}
                aria-labelledby="modal-modal-title"
                aria-describedby="modal-modal-description"
            >
                <Box sx={style}>
                    <div style={{ textAlign: "right" }}>
                        <IconButton onClick={() => {setOpen(false);}}>
                            <CloseIcon/>
                        </IconButton>
                    </div>
                    <QRBox/>
                </Box>
            </Modal>
        </Box>
    )
}