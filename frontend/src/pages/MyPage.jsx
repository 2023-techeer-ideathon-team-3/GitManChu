import {
    Box, IconButton, Modal, Typography
} from '@mui/material';
import InfoBox from '../components/MyPage/InfoBox';
import MainProfileBox from '../components/MyPage/MainProfileBox';
import React from 'react';
import QRBox from '../components/MyPage/QRBox';
import CropFreeIcon from '@mui/icons-material/CropFree';
import CloseIcon from '@mui/icons-material/Close';

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

export default function MyPage() {
    const [open, setOpen] = React.useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);

    return(
        <Box>
            {/* <Main/> */}
            <IconButton onClick={handleOpen} sx={{display: 'flex', alignItems: 'flex-end'}}>
                <CropFreeIcon/>
            </IconButton>

            <MainProfileBox/>

            <InfoBox/>
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