import { Box, Modal,IconButton,CardHeader,Avatar,Paper, InputBase, Toolbar, Typography, Grid, Card, CardContent,CardMedia,Container,Button,CardActions } from '@mui/material'
import SearchIcon from '@mui/icons-material/Search';
import GitHubIcon from '@mui/icons-material/GitHub';
import CloseIcon from '@mui/icons-material/Close';
import {useState} from 'react';
import PostDetailPage from '../components/MainPage/PostDetailPage';

const cards = [1, 2, 3, 4, 5, 6, 7, 8];

const style = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: 800,
    height: 600,
    bgcolor: 'background.paper',
    borderRadius: '20px',
    boxShadow: 24,
    p: 4,
};

export default function MainPage() {
    const [postTitle, setPostTitle] = useState('');
    const postTitleHandler = (e) => {
        setPostTitle(e.target.value);
    };

    const [open, setOpen] = useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);

    function didList() {
        var array = [];
    
        for (let index = 0; index < Object.keys(cards).length; index++) {
          array.push(
            <Grid item key={index} xs={12} sm={6} md={3}>
              <Card
                sx={{
                  height: "fit-content",
                  display: "flex",
                  flexDirection: "column",
                  borderRadius: 5,
                  "&:hover": {cursor: 'pointer'}
                }}
                onClick={handleOpen}    
              >
                <Toolbar>
                  <Box style={{ marginLeft: "-30px" }}>
                    <CardHeader
                      avatar={
                        <Avatar>
                          <GitHubIcon />
                        </Avatar>
                      }
                    />
                  </Box>
                  <Typography
                      variant="h6"
                      component="h2"
                      sx={{
                          mt: "-20px",
                          ml: -2,
                          color: "#6a6a6a",
                          fontSize: '18px'
                      }}
                      fontFamily="cookierun-bold"
                  >
                      헬로
                  </Typography>
                </Toolbar>
                <Typography
                      sx={{
                          color: "#ADADAD",
                          mt: "-34px",
                          mb: "0px",
                          ml: 8.5,
                          fontSize: '16px'
                      }}
                      fontFamily="cookierun-regular"
                  >
                      
                    gitmanchu11
                </Typography>
                <CardMedia
                  component="img"
                  height="194"
                //   image={emojiResult[index].image}
                  sx={{marginTop: 1}}
                />
                
              </Card>
            </Grid>
          );
        }
        return array;
    }

    return (
        <Box>
            <Toolbar>
                <Typography sx={{ml: 10}} fontSize='20pt' fontWeight='bold'>
                    메이트 찾기
                </Typography>
                <Paper
                    component="form"
                    sx={{ ml: 80, p: '2px 4px', display: 'flex', alignItems: 'center', width: 400, height: 40, borderRadius: 10 }}
                >
                    <SearchIcon sx={{ml: 1, color: '#BDB9B9'}}/>
                    <InputBase
                        sx={{ ml: 1, flex: 1 }}
                        placeholder="Write Down Your Fashion Title"
                        value={postTitle}
                        onChange={e => postTitleHandler(e)}
                    />
                </Paper>
            </Toolbar>

            <Container sx={{ py: 8 }} maxWidth='lg'>
                {/* End hero unit */}
                <Grid
                    container
                    spacing={4}
                    direction="row"
                    justifyContent="space-evenly"
                >
                    {didList()}
                </Grid>
            </Container>
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
                    <PostDetailPage/>
                </Box>
            </Modal>
        </Box>
    )
}