@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}f@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}m@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}f@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}a@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}a@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}m@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}A@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}P@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}I@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}R@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers},@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}H@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}T@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}T@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}P@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}E@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}x@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}c@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}
@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}f@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}m@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}a@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}.@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}a@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}.@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}d@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}m@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}S@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}D@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers},@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}C@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}U@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}
@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}f@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}m@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}q@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}l@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}a@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}l@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}c@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}h@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}m@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}y@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}m@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}l@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}c@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}
@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}f@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}m@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}a@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}.@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}m@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}d@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}l@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}.@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}b@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}m@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}B@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}
@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}f@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}m@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}a@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}.@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}a@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}.@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}f@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}_@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}m@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}f@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}_@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}
@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}m@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}d@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}
@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}f@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}m@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}a@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}.@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}c@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}h@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}m@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}a@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}.@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}b@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}m@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}B@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}C@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}a@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers},@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}B@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}R@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}
@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}f@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}m@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}a@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}.@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}v@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}c@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}.@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}b@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}m@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}b@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}_@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}v@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}c@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}
@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}m@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}d@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}
@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}
@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}=@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}A@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}P@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}I@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}R@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}(@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers})@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}
@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}
@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}@@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}.@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}(@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}"@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}/@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}"@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers},@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}_@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}m@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}d@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}l@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}=@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}B@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}R@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers})@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}
@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}a@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}y@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}c@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}d@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}f@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}_@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}b@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}(@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}d@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}b@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}:@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}S@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}D@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers},@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}c@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}_@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}:@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}C@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}U@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers},@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}b@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}_@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}:@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}B@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}C@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}a@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers})@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}:@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}
@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}y@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}:@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}
@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}b@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}=@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}a@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}w@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}a@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}b@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}_@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}v@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}c@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}.@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}_@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}b@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}(@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}
@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}d@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}b@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers},@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}
@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}b@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}_@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}=@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}b@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}_@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers},@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}
@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}d@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}_@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}b@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}y@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}=@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}c@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}_@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}.@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}d@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}
@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers})@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}
@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}#@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}H@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}w@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}w@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}l@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}l@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}v@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}a@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}l@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}l@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}y@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}h@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}C@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}l@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}y@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}b@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}a@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}c@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}k@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}d@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}a@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}k@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}f@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}A@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}I@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}A@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}a@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}l@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}y@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}(@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}P@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}h@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}a@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}4@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers})@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}
@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}b@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}
@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}x@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}c@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}V@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}a@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}l@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}E@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}a@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}:@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}
@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}a@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}H@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}T@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}T@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}P@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}E@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}x@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}c@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}(@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}a@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}_@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}c@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}d@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}=@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}4@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}0@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}0@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers},@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}d@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}a@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}l@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}=@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}(@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers})@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers})@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}
@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}
@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}@@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}.@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}(@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}"@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}/@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}{@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}b@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}_@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}d@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}}@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}"@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers},@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}_@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}m@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}d@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}l@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}=@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}B@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}R@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers})@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}
@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}a@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}y@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}c@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}d@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}f@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}_@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}b@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}(@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}d@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}b@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}:@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}S@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}D@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers},@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}c@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}_@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}:@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}C@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}U@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers},@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}b@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}_@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}d@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}:@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}d@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}.@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}U@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}U@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}I@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}D@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers})@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}:@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}
@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}b@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}=@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}a@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}w@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}a@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}b@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}_@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}v@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}c@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}.@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}(@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}d@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}b@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers},@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}d@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}=@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}b@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}_@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}d@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers})@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}
@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}f@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}b@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}:@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}
@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}a@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}H@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}T@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}T@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}P@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}E@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}x@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}c@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}p@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}(@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}a@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}s@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}_@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}c@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}d@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}=@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}4@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}0@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}4@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers},@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}d@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}a@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}i@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}l@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}=@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}"@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}B@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}f@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}o@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}d@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}"@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers})@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}
@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}e@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}t@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}r@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}n@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers} @router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}b@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}u@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}g@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}
@router.post("/{bug_id}/recommend")
async def recommend_developers(
    db: SessionDep, 
    bug_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers the Hybrid Fusion Engine to rank and recommend developers for a specific bug.
    """
    # Fetch the bug with BOLA protection
    bug = await bug_service.repository.get_tenant_safe(db, id=bug_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
        
    ranked_developers = await fusion_engine.recommend_developers(
        db=db,
        bug_title=bug.title,
        bug_description=bug.description,
        workspace_id=bug.workspace_id
    )
    
    return {"bug_id": bug_id, "recommendations": ranked_developers}